def programA(db, email, log):
  Result = db.getData()

  if Result > 0:
    email.Send(Result)
  else:
    log.write(Result)
