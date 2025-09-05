from django.shortcuts import render
from django.http import HttpResponse

def landing_page(request):
    # Beautiful landing page with premium icons and UI
    return HttpResponse('''
    <html>
    <head>
        <title>🛡️ ALX Backend Security</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            body { font-family: 'Segoe UI', Arial, sans-serif; background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%); margin: 0; }
            .container { max-width: 600px; margin: 60px auto; background: #fff; border-radius: 16px; box-shadow: 0 8px 32px rgba(0,0,0,0.12); padding: 40px; text-align: center; }
            h1 { font-size: 2.5em; margin-bottom: 0.2em; }
            .icons { font-size: 2em; margin-bottom: 1em; color: #0077b6; }
            .features { text-align: left; margin: 2em 0; }
            .features li { margin: 1em 0; font-size: 1.2em; }
            .footer { margin-top: 2em; color: #888; font-size: 1em; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="icons">
                <i class="fa-solid fa-shield-halved"></i>
                <i class="fa-solid fa-globe"></i>
                <i class="fa-solid fa-gauge-high"></i>
                <i class="fa-solid fa-user-secret"></i>
            </div>
            <h1>🛡️ ALX Backend Security</h1>
            <p>Premium Django security features for modern web apps.</p>
            <ul class="features">
                <li><i class="fa-solid fa-ban"></i> <b>IP Blacklisting</b> – Block malicious IPs</li>
                <li><i class="fa-solid fa-location-dot"></i> <b>Geolocation Analytics</b> – Track country & city</li>
                <li><i class="fa-solid fa-gauge-high"></i> <b>Rate Limiting</b> – Prevent abuse</li>
                <li><i class="fa-solid fa-user-secret"></i> <b>Anomaly Detection</b> – Flag suspicious activity</li>
            </ul>
            <div class="footer">
                <span>Made with <i class="fa-solid fa-heart" style="color:#e63946;"></i> for learning & security best practices.</span>
            </div>
        </div>
    </body>
    </html>
    ''')
from django.http import HttpResponse
from django.shortcuts import render
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='10/m', method='POST', block=True)
@ratelimit(key='ip', rate='5/m', method='GET', block=True)
def login_view(request):
    if getattr(request, 'limited', False):
        return HttpResponse("Rate limit exceeded. Try again later.", status=429)
    # ...your login logic here...
    return HttpResponse("Login page or login successful.")
