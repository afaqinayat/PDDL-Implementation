(define (problem PAG-problem1)
  (:domain PAG)
  (:objects
    user1
    bad-email
    gmail
    phishing-site
    account-bank
    vulnerability-phishing
    compromised-site
    file-with-trojan
    key-logger1
    crafted-email
    vbscript-link
    VB-5-1
    browser-IE
    vulnerability-key-logger
    browser-firefox
    malicious-certificate
    VB-5-6
    VB-5-7
    VB-5-8
    F1
    browser-seamonkey
    browser-mozilla)

  (:init
    (user user1)
    (mailer gmail)
    (exploit-vulnerability vulnerability-key-logger)
    (file file-with-trojan)
    (has-trojan file-with-trojan)
    (key-logger key-logger1)
    (key-logger-trojan file-with-trojan key-logger1)
    (site vbscript-link)
    (has-crafted-dialog-box vbscript-link)
    (vb-script-version VB-5-1)
    (software browser-IE)
    (browser browser-IE)
    (software browser-firefox)
    (= (version browser-firefox) 2)
    (browser browser-firefox)
    (information-available user1 account-bank)
    (account account-bank))

  (:goal (and (information-leakage account-bank))))
