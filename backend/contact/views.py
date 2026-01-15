from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import ContactMessage, NewsletterSubscriber


@csrf_exempt
@require_http_methods(["POST"])
def contact_submit(request):
    """
    API endpoint to receive contact form submissions
    """
    try:
        data = json.loads(request.body)
        
        # Validate required fields
        required_fields = ['name', 'email']
        for field in required_fields:
            if not data.get(field):
                return JsonResponse({
                    'success': False,
                    'message': f'{field.capitalize()} is required.'
                }, status=400)
        
        # Validate email format
        email = data.get('email', '').strip()
        if '@' not in email or '.' not in email:
            return JsonResponse({
                'success': False,
                'message': 'Please enter a valid email address.'
            }, status=400)
        
        # Create contact message
        contact_message = ContactMessage.objects.create(
            name=data.get('name', '').strip(),
            email=email,
            phone=data.get('phone', '').strip() or None,
            service=data.get('service', '').strip() or '',
            message=data.get('message', '').strip() or ''
        )
        
        # Print to console for debugging
        print("\n" + "="*50)
        print("NEW CONTACT MESSAGE RECEIVED")
        print("="*50)
        print(f"Name: {contact_message.name}")
        print(f"Email: {contact_message.email}")
        print(f"Phone: {contact_message.phone or 'N/A'}")
        print(f"Service: {contact_message.service}")
        print(f"Message: {contact_message.message}")
        print(f"Received at: {contact_message.created_at}")
        print("="*50 + "\n")
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you for your message! We\'ll get back to you soon.'
        }, status=201)
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid JSON data.'
        }, status=400)
    except Exception as e:
        print(f"Error processing contact form: {str(e)}")
        return JsonResponse({
            'success': False,
            'message': 'An error occurred. Please try again later.'
        }, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def newsletter_subscribe(request):
    """
    API endpoint to handle newsletter subscriptions
    """
    try:
        data = json.loads(request.body)
        email = data.get('email', '').strip()
        
        if not email:
            return JsonResponse({
                'success': False,
                'message': 'Email is required.'
            }, status=400)
        
        # Validate email format
        if '@' not in email or '.' not in email:
            return JsonResponse({
                'success': False,
                'message': 'Please enter a valid email address.'
            }, status=400)
        
        # Check if already subscribed
        subscriber, created = NewsletterSubscriber.objects.get_or_create(
            email=email,
            defaults={'is_active': True}
        )
        
        if not created:
            if subscriber.is_active:
                return JsonResponse({
                    'success': True,
                    'message': 'You are already subscribed to our newsletter!'
                })
            else:
                subscriber.is_active = True
                subscriber.save()
        
        print(f"\nNewsletter Subscription: {email}\n")
        
        return JsonResponse({
            'success': True,
            'message': 'Successfully subscribed to our newsletter!'
        }, status=201)
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid JSON data.'
        }, status=400)
    except Exception as e:
        print(f"Error processing newsletter subscription: {str(e)}")
        return JsonResponse({
            'success': False,
            'message': 'An error occurred. Please try again later.'
        }, status=500)

