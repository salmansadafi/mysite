class SEOHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # هدرهای مربوط به SEO و امنیت
        response['X-Robots-Tag'] = 'index, follow'
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        response['Content-Language'] = 'en'

        # هدرهای امنیتی مفید
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['Referrer-Policy'] = 'no-referrer-when-downgrade'
        response['Permissions-Policy'] = 'geolocation=(), microphone=()'  # برای محدود کردن دسترسی به قابلیت‌ها

        return response
