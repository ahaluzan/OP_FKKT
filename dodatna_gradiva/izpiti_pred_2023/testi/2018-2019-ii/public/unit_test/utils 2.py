
def compare_read_data(actual, expected, test_case):
    for player in expected.keys():
        test_case.assertIn(player, actual)

        for bet in expected[player]:
            test_case.assertIn(sorted(bet), sorted(actual[player]))

        for bet in actual[player]:
            test_case.assertIn(sorted(bet), sorted(expected[player]))

    for player in actual.keys():
        test_case.assertIn(player, expected)

        for bet in actual[player]:
            test_case.assertIn(sorted(bet), sorted(expected[player]))

        for bet in expected[player]:
            test_case.assertIn(sorted(bet), sorted(actual[player]))
