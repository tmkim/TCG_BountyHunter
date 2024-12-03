import datetime

from django.test import TestCase
from .models import Card


class QuestionModelTests(TestCase):
    def test_card_black(self):
        """
        is_black() returns True for cards whose color is black
        """
        test_card = Card(card_color='black') #add param to set card details
        self.assertIs(test_card.is_black(), True)

    '''
    Not going to fully write out tests yet. But going to start making list of what should be tested.

    User clicks on card -> card shows detail
        (maybe future -- card details show on the side of same view)
    Data in detail view matches data in database
    Filter functions
    Add up card costs
    Bounties are updated appropriately (check time period)
    Test color
    '''