

def parse_g_name(name):
    split_name = name.split("-")
    return ("{}{}".format(split_name[3], split_name[4])).lower()


def parse_a_dtype(desc):
    if "SSD" in desc:
        return "SSD"
    else:
        return "HDD"

def parse_location(loc):
    ploc = loc.split("(")[-1].split(")")[0]
    if "Virginia" in ploc:
        return "NVirginia"
    if "Carolina" in ploc:
        return "SCarolina"
    if "Paulo" in ploc:
        return "Sao_Paulo"
    if "California" in ploc:
        return "Northern_California"
    if "US" in ploc:
        return "GovCloud"
    if "Japan" in ploc:
        return "Tokyo"
    if "Osaka" in ploc:
        return "Tokyo"
    if "india" in ploc:
        return "Mumbai"
    if "United" in ploc:
        return "US"
    if "Pacific" in ploc:
        return "Asia_Pacific"
    return loc.split("(")[-1].split(")")[0]


def parse_cs(cs):
    return cs.split(" ")[0]


def parse_usg(usg):
    # print(usg.split(':')[1].split('.'))
    return "{}{}".format(usg.split(':')[1].split('.')[0], usg.split(':')[1].split('.')[1])




if __name__ == "__main__":
    name = "CP-COMPUTEENGINE-VMIMAGE-N1-HIGHMEM-4"
    loc = "US East (N. Virginia)"
    loc2 = ['Asia Pacific (Mumbai)', 'Any', 'South America (Sao Paulo)', 'Europe', 'Australia', 'EU (Paris)', 'US ISO East', 'EU (Ireland)', 'South America', 'Asia Pacific (Sydney)', 'US ISOB East (Ohio)', 'United States', 'Asia Pacific (Seoul)', 'Canada', 'EU (London)', 'EU (Frankfurt)', 'India', 'Asia Pacific (Singapore)', 'Japan', 'Asia Pacific (Tokyo)', 'US West (N. California)', 'US East (N. Virginia)', 'Asia Pacific', 'Canada (Central)', 'AWS GovCloud (US)', 'Asia Pacific (Osaka-Local)', 'US West (Oregon)', 'US East (Ohio)']
    csl = ['2.5 GHz', '2.3 GHz', '3.0 Ghz', '2.4 GHz', '2.9 GHz']
    usg = 'EUW2-DedicatedUsage:c4.xlarge'
    print(parse_g_name(name))

    d1 = "1 x 1920 SSD"
    d2 = "ebsonly"
    d3 = "1 x 1920 HDD"

    print(parse_a_dtype(d1))
    print(parse_a_dtype(d2))
    print(parse_a_dtype(d3))

    print(parse_location(loc))

    for el in loc2:
        print(parse_location(el))

    for el in csl:
        print(parse_cs(el))

    print(parse_usg(usg))
