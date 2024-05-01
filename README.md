# Tour De France
In here Our goal is to simulate the Tour de France race.

The Tour de France was first held in 1903 and has become an annual event, except for a few years during the World Wars.
The race consists of around 21 day-long stages, which include a mix of flat stages, mountain stages, time trials, and sprint stages. The total distance covered is usually around 3,500 kilometers.
The race is open to professional cycling teams, with each team typically consisting of 8-9 riders. Riders compete both individually and as part of their team.
The primary objective is to be the first rider to cross the finish line of the entire race, known as the "General Classification." Riders also compete for other secondary titles, such as the King of the Mountains (best climber) and the Points Classification (best sprinter).
The Tour de France is considered one of the most physically demanding sports events in the world. It attracts the best cyclists from around the globe, and winning the Tour is seen as a major achievement in a cyclist's career.
The Tour de France is one of the most widely watched sporting events, with millions of spectators lining the roads and billions of television viewers worldwide.
In summary, the Tour de France is an iconic bicycle race that tests the physical and mental limits of the world's top cyclists, making it a truly remarkable sporting event.

In this code we simulate each day in the __race()__ where its arguments are name of the country, speed of that country, day and the period. First three are clear but the last one is just because we need a shared data that help us to find the winner.

We simulate all the competition in a __for loop__. We use that in range 21 that is number of days and each day we create 8 processes that every process has a country name, speed, number of day, a shared data and target function of race. In this way we simulate all the competition and every day we update the times of each country in the competition and at the end of the code we will show the winner.(Top three)
