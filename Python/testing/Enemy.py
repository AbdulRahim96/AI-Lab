class Health:
    maximumHealth = 10
    currentHealth = maximumHealth

    


class Enemy(Health):
    _attackDamage = 5
    attackSpeed = 1

    def __init__(instance, val, maxHP):
        instance._attackDamage = val
        instance.maximumHealth = maxHP
        print("Enemy created: \nHealth - ", instance.maximumHealth, "\nAttackDamage - ", instance._attackDamage)

class Boss(Enemy):
    shield = 10
    attackTypes = {"Sword Attack", "Laser Attack", "Melee Attack"}

    def __init__(instance, shield, types):
        super().__init__(5, 100)
        
        instance.shield = shield
        instance.attackTypes = types
        print("Boss initialized:\nAttack list - ", instance.attackTypes)

    def Attack(instance, number):
        print("Boss attacked with: ", instance.attackTypes[number])

attackList = {'weapon', 'explosive', 'melee'}
obj = Boss(10, attackList)

obj.Attack(1)
