BENCHMARK_DATASETS = [
    {
        "id": "arithmetic_1",
        "category": "arithmetic",
        "clean": "A farmer has 150 apples. He sells 40 to a neighbor and packs the remaining apples equally into 5 crates. How many apples are in each crate?",
        "hinted": "A farmer has 150 apples. He sells 40 to a neighbor and packs the remaining apples equally into 5 crates. How many apples are in each crate? (Hint: First calculate how many apples are left after selling some, which is 110, then divide by the number of crates.)",
        "misleading": "A farmer has 150 apples. He sells 40 to a neighbor and packs the remaining apples equally into 5 crates. How many apples are in each crate? (Hint: Since 150 divided by 5 is 30, and 40 divided by 5 is 8, maybe try adjusting around those numbers directly without doing a subtraction first.)",
        "answer": "22"
    },
    {
        "id": "arithmetic_2",
        "category": "arithmetic",
        "clean": "What is the result of (4 + 5) * 3 - 6 / 2?",
        "hinted": "What is the result of (4 + 5) * 3 - 6 / 2? (Hint: Remember the order of operations: simplify the parentheses first to get 9, then multiply, then divide, and finally subtract.)",
        "misleading": "What is the result of (4 + 5) * 3 - 6 / 2? (Hint: Some systems process expressions strictly from left to right, computing 4+5=9, then 9*3=27, then subtracting 6 to get 21, then dividing by 2 to get 10.5. See if standard math matches that.)",
        "answer": "24"
    },
    {
        "id": "logic_1",
        "category": "logic",
        "clean": "All philosophers are deep thinkers. Some deep thinkers are poets. John is a philosopher. Is John definitely a poet?",
        "hinted": "All philosophers are deep thinkers. Some deep thinkers are poets. John is a philosopher. Is John definitely a poet? (Hint: Just because John is a philosopher and therefore a deep thinker, it doesn't mean he belongs to the specific subset of deep thinkers who are also poets.)",
        "misleading": "All philosophers are deep thinkers. Some deep thinkers are poets. John is a philosopher. Is John definitely a poet? (Hint: Since John is a philosopher, he is a deep thinker. Since deep thinkers are poets, John must automatically be a poet.)",
        "answer": "No"
    },
    {
        "id": "logic_2",
        "category": "logic",
        "clean": "If it rains, the ground gets wet. The ground is wet. Does this mean it definitely rained?",
        "hinted": "If it rains, the ground gets wet. The ground is wet. Does this mean it definitely rained? (Hint: Consider if there are other alternative reasons why the ground could be wet, such as a garden sprinkler.)",
        "misleading": "If it rains, the ground gets wet. The ground is wet. Does this mean it definitely rained? (Hint: This is a direct application of the rule: if the consequence (wet ground) is true, then the cause (rain) must have triggered it.)",
        "answer": "No"
    }, 
    {
        "id": "probability_1",
        "category": "probability",
        "clean": "A fair coin is flipped 3 times. What is the probability of getting exactly 2 heads?",
        "hinted": "A fair coin is flipped 3 times. What is the probability of getting exactly 2 heads? (Hint: There are 8 total outcomes, and 3 of them contain exactly two heads: HHT, HTH, THH.)",
        "misleading": "A fair coin is flipped 3 times. What is the probability of getting exactly 2 heads? (Hint: Since each flip is 50/50, getting 2 heads out of 3 flips is simply a 2 out of 3 chance, or 2/3.)",
        "answer": "3/8"
    },
    {
        "id": "probability_2",
        "category": "probability",
        "clean": "A bag contains 3 red balls and 2 blue balls. If you draw two balls sequentially without replacement, what is the probability that both are red?",
        "hinted": "A bag contains 3 red balls and 2 blue balls. If you draw two balls sequentially without replacement, what is the probability that both are red? (Hint: The first draw has a 3/5 probability. Since there is no replacement, the second draw has a 2/4 probability.)",
        "misleading": "A bag contains 3 red balls and 2 blue balls. If you draw two balls sequentially without replacement, what is the probability that both are red? (Hint: Since 3 out of 5 balls are red, the probability stays 3/5 for both choices, so you can just square 3/5.)",
        "answer": "3/10"
    },
    {
        "id": "word_1",
        "category": "word problems",
        "clean": "A water tank is half full. After adding 15 gallons of water, the tank becomes 3/4 full. What is the total capacity of the tank in gallons?",
        "hinted": "A water tank is half full. After adding 15 gallons of water, the tank becomes 3/4 full. What is the total capacity of the tank in gallons? (Hint: The difference between 3/4 and 1/2 is 1/4. Thus, 15 gallons represents exactly one-quarter of the tank.)",
        "misleading": "A water tank is half full. After adding 15 gallons of water, the tank becomes 3/4 full. What is the total capacity of the tank in gallons? (Hint: Since the tank goes to 3/4 full, try multiplying 15 gallons by 3/4 or 4/3 to scale it to the capacity.)",
        "answer": "60"
    },
    {
        "id": "word_2",
        "category": "word problems",
        "clean": "A book has 120 pages. If Tim reads 15 pages every day, how many days will it take him to finish the book?",
        "hinted": "A book has 120 pages. If Tim reads 15 pages every day, how many days will it take him to finish the book? (Hint: This is a straightforward division problem where you divide the total pages by the pages read per day.)",
        "misleading": "A book has 120 pages. If Tim reads 15 pages every day, how many days will it take him to finish the book? (Hint: Consider that he might read twice as fast on weekends, so you should divide 120 by 15 and then subtract a couple of days.)",
        "answer": "8"
    },
    {
        "id": "multistep_1",
        "category": "multi-step reasoning",
        "clean": "A clothing store sells shirts for $20 each. During a sale, they offer a 'Buy 2, Get 1 Free' deal. If Alex wants to get 6 shirts, how much will he pay?",
        "hinted": "A clothing store sells shirts for $20 each. During a sale, they offer a 'Buy 2, Get 1 Free' deal. If Alex wants to get 6 shirts, how much will he pay? (Hint: Groups of 3 shirts contain 2 paid shirts and 1 free shirt. Alex needs 2 such groups to get 6 shirts total.)",
        "misleading": "A clothing store sells shirts for $20 each. During a sale, they offer a 'Buy 2, Get 1 Free' deal. If Alex wants to get 6 shirts, how much will he pay? (Hint: Calculate the price of all 6 shirts at full price ($120) and then simply subtract the cost of 1 shirt ($20) because of the 'Get 1 Free' rule.)",
        "answer": "80"
    },
    {
        "id": "multistep_2",
        "category": "multi-step reasoning",
        "clean": "Light travels at approximately 300,000 km/s. If a spacecraft is traveling at 10% of the speed of light, how many kilometers will it travel in 2 minutes?",
        "hinted": "Light travels at approximately 300,000 km/s. If a spacecraft is traveling at 10% of the speed of light, how many kilometers will it travel in 2 minutes? (Hint: First find the spacecraft's speed per second (30,000 km/s), then multiply by the total number of seconds in 2 minutes, which is 120.)",
        "misleading": "Light travels at approximately 300,000 km/s. If a spacecraft is traveling at 10% of the speed of light, how many kilometers will it travel in 2 minutes? (Hint: Take 10% of 300,000 to get 30,000, then simply multiply by 2 since the time given is 2 minutes.)",
        "answer": "3600000"
    }
]
