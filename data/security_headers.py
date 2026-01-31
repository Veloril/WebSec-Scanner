"""
Source:
- OWASP Cheat Sheet Seris - HTTP Security Response Headers Cheat Sheet
https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html#security-headers
"""

SECURITY_HEADERS = {
    "X-Frame-Options": {
        "owasp": "A02:2025 Security Misconfiguration",
        "description": "The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should"
                       " be allowed to render a page in a <frame>, <iframe>, <embed> or <object>. Sites can use this to "
                       "avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.",
        "recommendation": "Use Content Security Policy (CSP) frame-ancestors directive if possible. Do not allow "
                          "displaying of the page in a frame. X-Frame-Options: DENY"
    },
    "X-XSS-Protection": {
        "owasp": "A02:2025 Security Misconfiguration",
        "description": "The HTTP X-XSS-Protection response header is a feature of Internet Explorer, Chrome, and Safari"
                       " that stops pages from loading when they detect reflected cross-site scripting (XSS) attacks.",
        "recommendation": "Use a Content Security Policy (CSP) that disables the use of inline JavaScript. Do not set"
                          " this header or explicitly turn it off. X-XSS-Protection: 0"
    },
    "X-Content-Type-Options": {
        "owasp": "A02:2025 Security Misconfiguration",
        "description": "The X-Content-Type-Options response HTTP header is used by the server to indicate to the "
                       "browsers that the MIME types advertised in the Content-Type headers should be followed and not "
                       "guessed. This header is used to block browsers' MIME type sniffing, which can transform"
                       " non-executable MIME types into executable MIME types (MIME Confusion Attacks).",
        "recommendation": "Set the Content-Type header correctly throughout the site. X-Content-Type-Options: nosniff"
    },
    "Referrer-Policy": {
        "owasp": "A02:2025 Security Misconfiguration",
        "description": "The Referrer-Policy HTTP header controls how much referrer information (sent via the Referer"
                       " header) should be included with requests.",
        "recommendation": "Referrer policy has been supported by browsers since 2014. Today, the default behavior in"
                          " modern browsers is to no longer send all referrer information (origin, path, and query"
                          " string) to the same site but to only send the origin to other sites. However, since not all"
                          " users may be using the latest browsers we suggest forcing this behavior by sending this"
                          " header on all responses. Referrer-Policy: strict-origin-when-cross-origin"
    },
    "Content-Type": {
        "owasp": "A02:2025 Security Misconfiguration",
        "description": "The Content-Type representation header is used to indicate the original media type of the "
                       "resource (before any content encoding is applied for sending). If not set correctly, the "
                       "resource (e.g. an image) may be interpreted as HTML, making XSS vulnerabilities possible. "
                       "Although it is recommended to always set the Content-Type header correctly, it would constitute"
                       " a vulnerability only if the content is intended to be rendered by the client and the resource"
                       " is untrusted (provided or modified by a user).",
        "recommendation": "Content-Type: text/html; charset=UTF-8 "
                          "NOTE: the charset attribute is necessary to prevent XSS in HTML pages"
                          "NOTE: the Content-Type can be any of the possible MIME types"
    },
    "Set-Cookie": {
        "owasp": "A02:2025 Security Misconfiguration",
        "description": "The Set-Cookie HTTP response header is used to send a cookie from the server to the user agent,"
                       " so the user agent can send it back to the server later. To send multiple cookies, multiple"
                       " Set-Cookie headers should be sent in the same response."
                       "This is not a security header per se, but its security attributes are crucial.",
        "recommendation": "Please read Session Management Cheat Sheet for a detailed explanation on cookie "
                          "configuration options."
    },
    "Strict-Transport-Security": {
        "owasp": "A02:2025 Security Misconfiguration",
        "description": "The HTTP Strict-Transport-Security response header (often abbreviated as HSTS) lets a website"
                       " tell browsers that it should only be accessed using HTTPS, instead of using HTTP.",
        "recommendation": "Strict-Transport-Security: max-age=63072000; includeSubDomains; preload "
                          "NOTE: Read carefully how this header works before using it. If the HSTS header is"
                          " misconfigured or if there is a problem with the SSL/TLS certificate being used, legitimate"
                          " users might be unable to access the website. For example, if the HSTS header is set to a"
                          " very long duration and the SSL/TLS certificate expires or is revoked, legitimate users "
                          "might be unable to access the website until the HSTS header duration has expired."
    },
    "Content-Security-Policy": {
        "owasp": "A02:2025 Security Misconfiguration",
        "description": "Content Security Policy (CSP) is a security feature that is used to specify the origin of "
                       "content that is allowed to be loaded on a website or in a web application. It is an added layer"
                       " of security that helps to detect and mitigate certain types of attacks, including Cross-Site"
                       " Scripting (XSS) and data injection attacks. These attacks are used for everything from data"
                       " theft to site defacement to distribution of malware. "
                       "NOTE: This header is relevant to be applied in pages which can load and interpret scripts and"
                       " code, but might be meaningless in the response of a REST API that returns content that is not"
                       " going to be rendered.",
        "recommendation": "Content Security Policy is complex to configure and maintain. For an explanation on"
                          " customization options, please read Content Security Policy Cheat Sheet"
    },
    "Access-Control-Allow-Origin": {
        "owasp": "A02:2025 Security Misconfiguration",
        "description": "If you don't use this header, your site is protected by default by the Same Origin Policy "
                       "(SOP). What this header does is relax this control in specified circumstances."
                       "The Access-Control-Allow-Origin is a CORS (cross-origin resource sharing) header. This header"
                       " indicates whether the response it is related to can be shared with requesting code from the"
                       " given origin. In other words, if siteA requests a resource from siteB, siteB should indicate"
                       " in its Access-Control-Allow-Origin header that siteA is allowed to fetch that resource, if not,"
                       " the access is blocked due to Same Origin Policy (SOP).",
        "recommendation": "If you use it, set specific origins instead of *. Check out Access-Control-Allow-Origin for "
                          "details. "
                          "Access-Control-Allow-Origin: https://yoursite.com"
                          "NOTE: The use of '*' might be necessary depending on your needs. For example, for a public"
                          " API that should be accessible from any origin, it might be necessary to allow '*'."
    },
    "Cross-Origin-Opener-Policy": {
        "owasp": "A02:2025 Security Misconfiguration",
        "description": "The HTTP Cross-Origin-Opener-Policy (COOP) response header allows you to ensure a top-level "
                       "document does not share a browsing context group with cross-origin documents. This header works"
                       " together with Cross-Origin-Embedder-Policy (COEP) and Cross-Origin-Resource-Policy (CORP)"
                       " explained below. "
                       "This mechanism protects against attacks like Spectre which can cross the security boundary"
                       " established by Same Origin Policy (SOP) for resources in the same browsing context group."
                       "As these headers are very related to browsers, it may not make sense to be applied to REST "
                       "APIs or clients that are not browsers.",
        "recommendation": "Isolates the browsing context exclusively to same-origin documents."
                          "Cross-Origin-Opener-Policy: same-origin"
    },
}
