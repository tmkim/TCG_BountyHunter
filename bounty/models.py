'''
productId,name,cleanName,imageUrl,categoryId,groupId,url,modifiedOn,imageCount,
lowPrice,midPrice,highPrice,marketPrice,directLowPrice,subTypeName,
extRarity,extNumber,extDescription,extColor,extCardType,extLife,extPower,extSubtypes,extAttribute,extCost,extCounterplus
'''

from django.db import models


class Bounties(models.Model):
    card_id = models.CharField(max_length=200)
    card_name = models.CharField(max_length=200)
    current_price = models.DecimalField(default=0.0, decimal_places=2, max_digits=20)
