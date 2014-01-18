from django.core.mail import send_mail

def enviarEmail(dados):
    message = '''
    Enviado por: {0}\n
    Mensagem: {1}
    '''.format(dados['email'], dados['mensagem'])
    send_mail(dados['assunto'], message, dados['email'], ['marcos_costa.sjc@hotmail.com'], fail_silently=False)