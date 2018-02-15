

def parse_g_name(name):
    split_name = name.split("-")
    return ("{}{}".format(split_name[3], split_name[4])).lower()


def parse_a_dtype(desc):
    if "SSD" in desc:
        return "SSD"
    else:
        return "HDD"


if __name__ == "__main__":
    name = "CP-COMPUTEENGINE-VMIMAGE-N1-HIGHMEM-4"
    print(parse_g_name(name))

    d1 = "1 x 1920 SSD"
    d2 = "ebsonly"
    d3 = "1 x 1920 HDD"

    print(parse_a_dtype(d1))
    print(parse_a_dtype(d2))
    print(parse_a_dtype(d3))