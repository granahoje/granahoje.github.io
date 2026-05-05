// Cookie Consent Banner - LGPD/GDPR Compliant
// Este script implementa um banner de consentimento de cookies que bloqueia scripts de rastreamento até o aceite

(function() {
    'use strict';

    const CONSENT_KEY = 'grana-hoje-cookie-consent';
    const CONSENT_VERSION = '1.0';

    // Verificar se o usuário já consentiu
    function hasConsent() {
        const consent = localStorage.getItem(CONSENT_KEY);
        return consent === 'accepted';
    }

    // Salvar consentimento
    function setConsent(accepted) {
        if (accepted) {
            localStorage.setItem(CONSENT_KEY, 'accepted');
            loadTrackingScripts();
        } else {
            localStorage.setItem(CONSENT_KEY, 'rejected');
        }
        hideBanner();
    }

    // Carregar scripts de rastreamento (Google Analytics e AdSense)
    function loadTrackingScripts() {
        // Google Analytics
        if (window.gtag) {
            gtag('consent', 'update', {
                'analytics_storage': 'granted',
                'ad_storage': 'granted'
            });
        }

        // Recarregar AdSense
        if (window.adsbygoogle) {
            (adsbygoogle = window.adsbygoogle || []).push({});
        }
    }

    // Criar e exibir o banner
    function createBanner() {
        const banner = document.createElement('div');
        banner.id = 'cookie-consent-banner';
        banner.innerHTML = `
            <div style="
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                background: rgba(15, 23, 42, 0.95);
                backdrop-filter: blur(12px);
                border-top: 1px solid rgba(255, 255, 255, 0.1);
                padding: 20px;
                z-index: 9999;
                font-family: 'Plus Jakarta Sans', sans-serif;
                color: #f8fafc;
            ">
                <div style="max-width: 1200px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
                    <div style="flex: 1; min-width: 250px;">
                        <p style="margin: 0 0 10px 0; font-weight: 700; color: #00d1b2;">🍪 Consentimento de Cookies</p>
                        <p style="margin: 0; font-size: 0.9rem; color: #94a3b8;">
                            Usamos cookies para melhorar sua experiência, analisar tráfego e exibir anúncios personalizados. 
                            Leia nossa <a href="/privacy-policy.html" style="color: #00d1b2; text-decoration: underline;">Política de Privacidade</a> 
                            para mais informações.
                        </p>
                    </div>
                    <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                        <button id="cookie-reject" style="
                            padding: 10px 20px;
                            background: rgba(255, 255, 255, 0.1);
                            border: 1px solid rgba(255, 255, 255, 0.2);
                            color: #f8fafc;
                            border-radius: 8px;
                            cursor: pointer;
                            font-weight: 600;
                            font-size: 0.9rem;
                            transition: all 0.3s;
                        ">Rejeitar</button>
                        <button id="cookie-accept" style="
                            padding: 10px 20px;
                            background: #00d1b2;
                            border: none;
                            color: #0f172a;
                            border-radius: 8px;
                            cursor: pointer;
                            font-weight: 700;
                            font-size: 0.9rem;
                            transition: all 0.3s;
                        ">Aceitar Cookies</button>
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
    }

    // Ocultar banner
    function hideBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        if (banner) {
            banner.style.opacity = '0';
            banner.style.transition = 'opacity 0.3s';
            setTimeout(() => banner.remove(), 300);
        }
    }

    // Inicializar
    function init() {
        if (!hasConsent()) {
            // Bloquear Google Analytics e AdSense até consentimento
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('consent', 'default', {
                'analytics_storage': 'denied',
                'ad_storage': 'denied'
            });

            // Mostrar banner
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', createBanner);
            } else {
                createBanner();
            }
        } else {
            // Usuário já consentiu, carregar scripts
            loadTrackingScripts();
        }
    }

    // Iniciar quando o DOM estiver pronto
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
