(define (problem cloud_ransomware-problem)
  (:domain cloud_ransomware)

  (:objects
    attacker1 - attacker
    kms-key1 - kms-key
    target-bucket - s3-bucket
    file1 file2 file3 - object)

  (:init
    (attacker attacker1)
    (s3-bucket target-bucket)
    (object file1 target-bucket)
    (object file2 target-bucket)
    (object file3 target-bucket))

  (:goal
    (and (object-encrypted file1 kms-key1)
         (object-encrypted file2 kms-key1)
         (object-encrypted file3 kms-key1)
         (kms-key-deletion-scheduled kms-key1)
         (ransom-note-uploaded target-bucket)))
)
