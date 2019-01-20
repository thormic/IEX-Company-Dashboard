def FindName(issuetype):
    dictionary = {'ad' : 'American Depository Receipt (ADR’s)',
                  're' : 'Real Estate Investment Trust (REIT’s)',
                  'ce' : 'Closed end fund (Stock and Bond Fund)',
                  'si' : 'Secondary Issue',
                  'lp' : 'Limited Partnerships',
                  'cs' : 'Common Stock',
                  'et' : 'Exchange Traded Fund (ETF)',
                  ' ' : 'Not Available, i.e., Warrant, Note, or (non-filing) Closed Ended Funds'
                  }
    return dictionary.get(issuetype)
