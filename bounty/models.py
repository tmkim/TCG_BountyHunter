'''
productId,name,cleanName,imageUrl,categoryId,groupId,url,modifiedOn,imageCount,
lowPrice,midPrice,highPrice,marketPrice,directLowPrice,subTypeName,
extRarity,extNumber,extDescription,extColor,extCardType,extLife,extPower,extSubtypes,extAttribute,extCost,extCounterplus
'''

from datetime import timezone
import datetime
from django.contrib import admin
from django.db import models

'''
idea is that we have a database with 2 separate tables for Cards and Bounties
This way we can update bounties and cards separately without needing to take up all resources for separate updates
This is mostly bc we will be updating bounties daily but cards don't need to be updated frequently
so there will be a 1-1 relation with id as a foreign key on Bounty so we can look up Bounty from Card table
'''
    
class Card(models.Model):
# extRarity,extNumber,extDescription,extColor,extCardType,extLife,extPower,extSubtypes,extAttribute,extCost,extCounterplus
    name = models.CharField(max_length=200)
    market_price = models.DecimalField(decimal_places=2, max_digits=15)
    rarity = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)
    # etc ...

    def __str__(self):
        # return self.name
        return "{0} {1}-cost {2}".format(self.color, self.cost, self.name)
    
    def is_red(self):
        return self.color == 'red'
    
    def is_blue(self):
        return self.color == 'blue'
    
    def is_green(self):
        return self.color == 'green'
    
    def is_black(self):
        return self.color == 'black'
    
    def is_yellow(self):
        return self.color == 'yellow'
    
    def is_purple(self):
        return self.color == 'purple'
    
    @admin.display(
        boolean=True,
        ordering="name",
        description="Cards",
    )
    
    def get_info(self):
        return {
            'name' : self.name,
            'market_price' :self.market_price,
            'rarity': self.rarity,
            'desc': self.desc,
            'color': self.color,
            'cost': self.cost,
        }
    
class Bounty(models.Model):
    card_id = models.ForeignKey(Card, on_delete=models.CASCADE)
    current_price = models.DecimalField(default=0.0, decimal_places=2, max_digits=20)
    previous_price = models.DecimalField(default=0.0, decimal_places=2, max_digits=20)
    last_updated = models.DateTimeField("Last Updated")

    def __str__(self):
        return "{0} -- {1}".format(self.card_id, self.current_price)
    
    def was_updated_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.last_updated <= now

    def get_price_diff(self):
        return self.current_price - self.previous_price