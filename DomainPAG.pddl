(define (domain Phishing)
(:requirements :equality :disjunctive-preconditions)

(:functions
(version ?software))


(:predicates
	(user ?User)
	(email-msg ?User ?Msg)
	(phishing-msg ?Msg ?Site)
	(mailer ?email-program)
	(use-software ?software)
	(msg-opened ?Msg)
	(successful)
	(clicked-link ?msg ?Site)
	(user-visits-site ?User ?Site)
	(exploit-vulnerability ?Vulnerability)
	(information-leakage ?Account)
	(account ?Acct)
	(has-link ?Email ?Site)
	(software ?program)
	(browser ?name)
	(site ?site)
	(user-types ?key)
	(running ?software)
	(file ?file)
	(system ?System)
        (system-secure ?System)
        (access-controlled ?System)
	(mail-attachment ?msg ?file)
	(opened ?file)
	(has-trojan ?File)
	(key-logger-trojan ?File ?Keylogger)
	(key-logger ?kl)
	(installed ?file)
	(has-crafted-dialog-box ?Site)
	(F1-dialog-box-opens ?Site)
	(vb-script-version ?num)
	(information-available ?User ?Account)
	(logged-in ?User ?Account)
	(records ?KeyLogger ?Account)
	(browser-ssl-compromised ?Browser)
	(certificate-authorized ?Certificate))


(:action attacker-sends-email-with-keylogger
:parameters (?User ?File ?Keylogger)
:precondition (and (user ?User) (file ?File)
(has-trojan ?File) (key-logger-trojan
?File ?Keylogger))
:effect (and (email-msg ?User bad-email)
(mail-attachment bad-email ?File)))

(:action user-visits-site
:parameters (?User ?Browser ?Site)
:precondition (and (user ?User) (software ?Browser)
(browser ?Browser) (site ?Site))
:effect (and (use-software ?Browser)
(user-visits-site ?User ?Site)))

(:action user-starts-email :parameters (?User ?Mailer)
:precondition (and (user ?User) (mailer ?Mailer))
:effect (and (use-software ?Mailer) (running ?Mailer)))

(:action user-reads-email
:parameters (?User ?Mailer ?Msg)
:precondition (and (user ?User) (mailer ?Mailer)
(use-software ?Mailer) (email-msg ?User ?Msg))
:effect (and (msg-opened ?Msg)))



(:action user-presses-F1-at-vbscript-site
:parameters (?User ?Browser ?Site)
:precondition (and (user ?User) (use-software ?Browser)
(browser ?Browser)
(= ?Browser browser-IE) (= ?Site vbscript-link)
(user-visits-site ?User vbscript-link))
:effect (user-types F1))

(:action user-opens-attachment
:parameters (?User ?Msg ?File ?Mailer)
:precondition (and (user ?User)
(use-software ?Mailer) (mailer ?Mailer)
(msg-opened ?Msg)
(mail-attachment ?Msg ?File) (file ?File))
:effect (opened ?File))

(:action key-logger-installed
:parameters (?User ?File ?KeyLogger)
:precondition (and (user ?User)
(opened ?File) (file ?File) (has-trojan ?File)
(key-logger-trojan ?File ?KeyLogger))
:effect (and (key-logger ?KeyLogger)
(installed ?KeyLogger)))

(:action key-logger-activated
:parameters (?KeyLogger ?Program)
:precondition (and (key-logger ?KeyLogger)
(installed ?KeyLogger)
(user-types F1) (use-software ?Program)
(= ?Program browser-IE))
:effect (running ?KeyLogger))

(:action attacker-intercepts
:parameters (?KeyLogger ?Account)
:precondition (and (records ?KeyLogger ?Account)
(exploit-vulnerability vulnerability-key-logger))
:effect (information-leakage ?Account))

(:action user-login-with-keylogger-activated
:parameters (?User ?Account ?Keylogger)
:precondition (and (user ?User) (account ?Account)
(key-logger ?Keylogger)
(running ?Keylogger))
:effect (and (logged-in ?User ?Account)
(information-available ?User ?Account)
(records ?Keylogger ?Account)))



 (:action remove-keylogger
    :parameters (?User ?Keylogger)
    :precondition (and (user ?User) (key-logger ?Keylogger) (running ?Keylogger))
    :effect (not (running ?Keylogger)))

  (:action secure-system
    :parameters (?User ?System)
    :precondition (and (user ?User) (system ?System))
    :effect (and (system-secure ?System)))

  (:action prevent-unauthorized-access
    :parameters (?User ?System)
    :precondition (and (user ?User) (system ?System) (running ?System))
    :effect (and (access-controlled ?System))))

