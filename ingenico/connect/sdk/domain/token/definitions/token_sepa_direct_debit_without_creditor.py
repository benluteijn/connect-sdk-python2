# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.token.definitions.abstract_token import AbstractToken
from ingenico.connect.sdk.domain.token.definitions.customer_token_with_contact_details import CustomerTokenWithContactDetails
from ingenico.connect.sdk.domain.token.definitions.mandate_sepa_direct_debit_without_creditor import MandateSepaDirectDebitWithoutCreditor


class TokenSepaDirectDebitWithoutCreditor(AbstractToken):

    __customer = None
    __mandate = None

    @property
    def customer(self):
        """
        | Object containing the details of the customer
        
        Type: :class:`ingenico.connect.sdk.domain.token.definitions.customer_token_with_contact_details.CustomerTokenWithContactDetails`
        """
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def mandate(self):
        """
        | Object containing the mandate details
        
        Type: :class:`ingenico.connect.sdk.domain.token.definitions.mandate_sepa_direct_debit_without_creditor.MandateSepaDirectDebitWithoutCreditor`
        """
        return self.__mandate

    @mandate.setter
    def mandate(self, value):
        self.__mandate = value

    def to_dictionary(self):
        dictionary = super(TokenSepaDirectDebitWithoutCreditor, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'customer', self.customer)
        self._add_to_dictionary(dictionary, 'mandate', self.mandate)
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenSepaDirectDebitWithoutCreditor, self).from_dictionary(dictionary)
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = CustomerTokenWithContactDetails()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'mandate' in dictionary:
            if not isinstance(dictionary['mandate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandate']))
            value = MandateSepaDirectDebitWithoutCreditor()
            self.mandate = value.from_dictionary(dictionary['mandate'])
        return self
