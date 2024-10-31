(define (domain cloud_ransomware)
  (:requirements :strips :typing :equality)

  (:predicates
    (attacker ?a)
    (kms-key ?key)
    (kms-key-exposed ?key)
    (kms-key-used ?key ?bucket)
    (kms-key-deletion-scheduled ?key)  ; Predicates that refer to key
    (s3-bucket ?bucket)
    (object ?object ?bucket)
    (has-write-access ?attacker ?bucket)
    (bucket-checked ?bucket)
    (object-encrypted ?object ?key)
    (ransom-note-uploaded ?bucket))

  ; Action 1: Attacker creates a KMS key
  (:action create-kms-key
    :parameters (?attacker ?key)
    :precondition (attacker ?attacker)
    :effect (kms-key ?key))

  ; Action 2: Attacker gains write access to an S3 bucket
  (:action gain-write-access
    :parameters (?attacker ?bucket)
    :precondition (s3-bucket ?bucket)
    :effect (has-write-access ?attacker ?bucket))

  ; Action 3: Attacker checks the configuration of the bucket
  (:action check-bucket-configuration
    :parameters (?attacker ?bucket)
    :precondition (has-write-access ?attacker ?bucket)
    :effect (bucket-checked ?bucket))

  ; Action 4: Attacker encrypts objects using KMS key
  (:action encrypt-objects
    :parameters (?attacker ?bucket ?key ?object)
    :precondition (and (has-write-access ?attacker ?bucket)
                       (bucket-checked ?bucket)
                       (kms-key ?key)
                       (object ?object ?bucket))
    :effect (and (object-encrypted ?object ?key)
                 (kms-key-used ?key ?bucket)))

  ; Action 5: Schedule KMS key deletion
  (:action schedule-kms-key-deletion
    :parameters (?attacker ?key ?bucket)
    :precondition (and (kms-key-used ?key ?bucket))
    :effect (kms-key-deletion-scheduled ?key))

  ; Action 6: Attacker uploads ransom note
  (:action upload-ransom-note
    :parameters (?attacker ?bucket ?key)  ; Added ?key here
    :precondition (and (has-write-access ?attacker ?bucket)
                       (kms-key-deletion-scheduled ?key))  ; Now this works
    :effect (ransom-note-uploaded ?bucket))
)
