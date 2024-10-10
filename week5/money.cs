// AddMoney helper.</summary>
public IMoney Add(IMoney m)
{
  return m.AddMoney(this)
}

public IMoney AddMoney(Money m)
{
  if (m.Currency.Equals(Currency) )
    return new Money(Amount+m.Amount, Currency);
  return newMoneyBag(this, m);
}

public IMoney AddMoneyBag(MoneyBag s)
{
  return s.AddMoney(this);
}