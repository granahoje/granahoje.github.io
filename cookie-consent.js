// Cookie Consent Banner - LGPD/GDPR Compliant
// Este script implementa um banner de consentimento de cookies que bloqueia scripts de rastreamento até o aceite
// Versão 2.1 - Corrigido para persistir tanto aceitação quanto rejeição

(function() {
    'use strict';

    const CONSENT_KEY = 'grana-hoje-cookie-consent';
    const CONSENT_VERSION = '2.1';
    const CONSENT_TIMESTAMP = 'grana-hoje-consent-timestamp';

    // Verificar se o usuário já fez uma escolha (aceitar ou rejeitar)
    function hasConsent() {
        const consent = localStorage.getItem(CONSENT_KEY);
        // O banner deve ficar oculto se houver QUALQUER escolha salva
        return consent === 'accepted' || consent === 'rejected';
    }

    // Verificar se o consentimento expirou (renovar a cada 30 dias)
    function isConsentExpired() {
        const timestamp = localStorage.getItem(CONSENT_TIMESTAMP);
        if (!timestamp) return true;
        
        const expiryTime = 30 * 24 * 60 * 60 * 1000; // 30 dias em ms
        return Date.now() - parseInt(timestamp) > expiryTime;
    }

    // Salvar consentimento
    function setConsent(accepted) {
        if (accepted) {
            localStorage.setItem(CONSENT_KEY, 'accepted');
            localStorage.setItem(CONSENT_TIMESTAMP, Date.now().toString());
            localStorage.setItem(CONSENT_VERSION, CONSENT_VERSION);
            
            // Atualizar consentimento do Google
            updateGoogleConsent(true);
            
            // Recarregar anúncios
            try {
                );
                }
            } catch (e) {
                console.error("Erro ao carregar anúncios após consentimento:", e);
            }
        } else {
            // Se rejeitado, salvamos 'rejected' para que o banner não apareça novamente
            localStorage.setItem(CONSENT_KEY, 'rejected');
            localStorage.setItem(CONSENT_TIMESTAMP, Date.now().toString());
            updateGoogleConsent(false);
        }
        hideBanner();
    }

    // Atualizar consentimento do Google
    function updateGoogleConsent(granted) {
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        
        gtag('consent', 'update', {
            'analytics_storage': granted ? 'granted' : 'denied',
            'ad_storage': granted ? 'granted' : 'denied',
            'ad_user_data': granted ? 'granted' : 'denied',
            'ad_personalization': granted ? 'granted' : 'denied'
        });
    }

    // Criar e exibir o banner
    function createBanner() {
        // Evitar duplicatas
        if (document.getElementById('cookie-consent-banner')) return;

        const banner = document.createElement('div');
        banner.id = 'cookie-consent-banner';
        banner.setAttribute('role', 'dialog');
        banner.setAttribute('aria-label', 'Cookie Consent');
        
        banner.innerHTML = `
            <div style="
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                background: rgba(15, 23, 42, 0.98);
                backdrop-filter: blur(12px);
                border-top: 2px solid rgba(0, 209, 178, 0.3);
                padding: 20px;
                z-index: 9999;
                font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                color: #f8fafc;
                box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.3);
            ">
                <div style="max-width: 1200px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
                    <div style="flex: 1; min-width: 250px;">
                        <p style="margin: 0 0 10px 0; font-weight: 700; color: #00d1b2; font-size: 1.05rem;">🍪 Consentimento de Cookies e Rastreamento</p>
                        <p style="margin: 0; font-size: 0.9rem; color: #cbd5e1; line-height: 1.5;">
                            Usamos cookies e tecnologias de rastreamento para melhorar sua experiência, analisar tráfego do site e exibir anúncios personalizados. 
                            Seus dados são protegidos conforme a LGPD e GDPR. Leia nossa 
                            <a href="/privacy-policy.html" style="color: #00d1b2; text-decoration: underline; font-weight: 600;">Política de Privacidade</a> 
                            para mais informações.
                        </p>
                    </div>
                    <div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: flex-end;">
                        <button id="cookie-reject" style="
                            padding: 12px 24px;
                            background: rgba(255, 255, 255, 0.1);
                            border: 1px solid rgba(255, 255, 255, 0.2);
                            color: #f8fafc;
                            border-radius: 8px;
                            cursor: pointer;
                            font-weight: 600;
                            font-size: 0.9rem;
                            transition: all 0.3s ease;
                            white-space: nowrap;
                        " onmouseover="this.style.background='rgba(255, 255, 255, 0.15)'" onmouseout="this.style.background='rgba(255, 255, 255, 0.1)'">
                            Rejeitar
                        </button>
                        <button id="cookie-accept" style="
                            padding: 12px 24px;
                            background: #00d1b2;
                            border: none;
                            color: #0f172a;
                            border-radius: 8px;
                            cursor: pointer;
                            font-weight: 700;
                            font-size: 0.9rem;
                            transition: all 0.3s ease;
                            white-space: nowrap;
                        " onmouseover="this.style.background='#00b89c'" onmouseout="this.style.background='#00d1b2'">
                            Aceitar Cookies
                        </button>
                    </div>
                </div>
            </div>
        `;
        document.body.appendChild(banner);

        // Event listeners
        document.getElementById('cookie-accept').addEventListener('click', function() {
            setConsent(true);
        });

        document.getElementById('cookie-reject').addEventListener('click', function() {
            setConsent(false);
        });

        // Fechar ao pressionar Escape
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') {
                setConsent(false);
            }
        });
    }

    // Ocultar banner
    function hideBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        if (banner) {
            banner.style.opacity = '0';
            banner.style.transition = 'opacity 0.3s ease';
            setTimeout(() => {
                if (banner.parentNode) {
                    banner.parentNode.removeChild(banner);
                }
            }, 300);
        }
    }

    // Inicializar
    function init() {
        // Verificar se o consentimento expirou
        if (isConsentExpired()) {
            localStorage.removeItem(CONSENT_KEY);
            localStorage.removeItem(CONSENT_TIMESTAMP);
        }

        if (!hasConsent()) {
            // Bloquear Google Analytics e AdSense até consentimento
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('consent', 'default', {
                'analytics_storage': 'denied',
                'ad_storage': 'denied',
                'ad_user_data': 'denied',
                'ad_personalization': 'denied'
            });

            // Mostrar banner
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', createBanner);
            } else {
                createBanner();
            }
        } else {
            // Usuário já fez uma escolha
            const consent = localStorage.getItem(CONSENT_KEY);
            updateGoogleConsent(consent === 'accepted');
            
            // Recarregar anúncios se AdSense estiver carregado e aceito
            try {
                );
                }
            } catch (e) {
                console.error("Erro ao carregar anúncios pré-existentes:", e);
            }
        }
    }

    // Função pública para revogar consentimento
    window.revokeConsent = function() {
        localStorage.removeItem(CONSENT_KEY);
        localStorage.removeItem(CONSENT_TIMESTAMP);
        location.reload();
    };

    // Iniciar quando o DOM estiver pronto
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
