states = ['Tennessee', 'Alabama', 'Mississippi', 'Georgia', 'Florida', 
          'Louisiana', 'Arkansas', 'Kentucky', 'Virginia', 'West Virginia',  
          'North Carolina', 'South Carolina', 'Maryland', 'Ohio', 'Pennsylvania', 
          'New Jersey', 'New York', 'Massachusetts', 'Rhode Island', 'Connecticut', 
          'Vermont', 'New Hampshire', 'Maine', 'Indiana', 'Illinois', 
          'Michigan', 'Wisconsin', 'Minnesota', 'Missouri', 'Texas', 
          'Oklahoma', 'Kansas', 'Nebraska', 'South Dakota', 'North Dakota', 
          'New Mexico', 'Colorado', 'Wyoming', 'Montana', 'Arizona', 
          'Utah', 'Idaho', 'Nevada', 'California', 'Oregon', 
          'Washington', 'Hawaii', 'Alaska', 'Delaware', 'Iowa']

capitals = ['Nashville', 'Montgomery', 'Jackson', 'Atlanta', 'Tallahassee', 
            'Baton Rouge', 'Little Rock', 'Frankfort', 'Richmond', 'Charleston', 
            'Raleigh', 'Columbia', 'Annapolis', 'Columbus', 'Harrisburg', 
            'Trenton', 'Albany', 'Boston', 'Providence', 'Hartford', 
            'Montpelier', 'Concord', 'Augusta', 'Indianapolis', 'Springfield', 
            'Lansing', 'Madison', 'Saint Paul', 'Jefferson City', 'Austin', 
            'Oklahoma City', 'Topeka', 'Lincoln', 'Pierre', 'Bismarck',
            'Santa Fe', 'Denver', 'Cheyenne', 'Helena', 'Phoenix', 
            'Salt Lake City', 'Boise', 'Carson City', 'Sacramento', 'Salem', 
            'Olympia', 'Honolulu', 'Juneau', 'Dover', 'Des Moines']

combined = list(zip(capitals, states))

for item in combined :
    print(item)
