#!/usr/bin/env python3

'''
Generer une chaine de cadeaux et envoyer un mail aux joueurs pour
leur désigner leur destinataire.
'''

import random
from collections import namedtuple
import smtplib
from email.mime.text import MIMEText

__author__ = 'Sebastien Julliot'
__email__ = 'julliot@ljll.math.upmc.fr'

User = namedtuple('User', ['first', 'mail'])

msg = ('Wesh {user.first},\n'
       '\n'
       'Santa t\'a désigné pour donner un cadeau à {give_to.first} cette année.\n'
       '\n'
       'Que le dauphin soit avec toi !')

message_subject = '[SANTA] Pour la chaine de cadeaux tu devras donner le tien à ... #LienPutaclic'

smtp_server = 'smtp.jdlm.tech'
from_mail = 'no-reply@jdlm.tech'
login = 'sebastien@jdlm.tech'
passwd = ''

server = smtplib.SMTP(smtp_server)
server.starttls()
server.login(login, passwd)

def send_mail(user, give_to, msg, subject):
    print ('Envoi à {}'.format(give_to.first))
    msg_text = msg.format(user=user, give_to=give_to)
    msg = MIMEText(msg_text, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = from_mail
    msg['To'] = user.mail

    server.sendmail(from_mail, [user.mail], msg.as_string())

def permute(l):
    copy = list(l)
    while any(copy[i] == l[i] for i in range(len(l))):
        random.shuffle(copy)
    return copy

nb = int(input('Combien de *joueurs* ? '))
print ('')
users = []
for i in range(nb):
    print ('Joueur ' + str(i))
    first = str(input('Prénom : '))
    mail = str(input('Mail : '))
    print ('')

    users.append(User(first, mail))

deranged = permute(users)
for user,give_to in zip(users, deranged):
    send_mail(user, give_to, msg, message_subject)
