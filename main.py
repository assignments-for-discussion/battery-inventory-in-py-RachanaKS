def count_batteries_by_usage(cycles):
    dict = {
        "lowCount": 0,
        "mediumCount": 0,
        "highCount": 0
    }
    for i in cycles:
        if i <= 400:
            dict["lowCount"] = dict["lowCount"] + 1  # incrementing the lowCount
        if 400 < i <= 919:
            dict["mediumCount"] = dict["mediumCount"] + 1  # incrementing the mediumCount
        if i >= 920:
            dict["highCount"] = dict["highCount"] + 1  # incrementing the highCount
    
    return dict


def test_bucketing_by_number_of_cycles():
    print("Counting batteries by usage cycles...\n");
    counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000, 400, 919, 920])  # adding boundary values
    assert (counts["lowCount"] == 3)
    assert (counts["mediumCount"] == 4)
    assert (counts["highCount"] == 2)
    print("Done counting :)")

    
if __name__ == '__main__':
    test_bucketing_by_number_of_cycles()
