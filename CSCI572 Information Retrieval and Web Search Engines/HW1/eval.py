import json

def manipulate_url(url):
    # Ignore "https://" and "http://" in the URL
    index = url.find("//")
    if index > -1:
        url = url[index + 2:]
    # Ignore "www." in the URL
    if "www." in url:
        url = url[4:]
    # Ignore "/" at the end of the URL
    if url[-1] == "/":
        url = url[:-1]
    return url


def calculate_rho(matching_url):
    # If there is no matching, Spearman coefficient is 0
    if len(matching_url) == 0:
        coefficient = 0
    # If there is exactly 1 matching
    elif len(matching_url) == 1:
        # If Google index and Yahoo index are the same, Spearman coefficient is 1, Otherwise, 0.
        if matching_url[0][0] == matching_url[0][1]:
            coefficient = 1
        else:
            coefficient = 0
    else:
        difference = sum([(a - b) ** 2 for a, b in matching_url])
        coefficient = 1 - ((6 * difference) / (len(matching_url) * (len(matching_url) ** 2 - 1)))
    return coefficient


def calculate_avg_stats(stats):
    avg_overlap, avg_percent_overlap, avg_coefficient = 0, 0, 0
    for _, value in stats.items():
        avg_overlap += value["Overlap"] / 100
        avg_percent_overlap += value["Percent"] / 100
        avg_coefficient += value["Rho"] / 100
    stats["Averages"] = {"Overlap": avg_overlap, "Percent": avg_percent_overlap, "Rho": avg_coefficient}


def write_result(stats):
    with open("hw1.csv", "w") as f:
        f.write("Queries, Number of Overlapping Results, Percent Overlap, Spearman Coefficient\n")
        i=1
        for query_number, values in stats.items():
            f.write(f"Query {i}, {values['Overlap']}, {values['Percent']}, {values['Rho']}\n")
            i += 1


f = open('google.json')
google_raw = json.load(f)
f.close()
f = open('hw1.json')
yahoo_raw = json.load(f)
f.close()

stats = {}
for key in yahoo_raw:
    google_clean = [manipulate_url(url) for url in google_raw[key]]
    yahoo_clean = [manipulate_url(url) for url in yahoo_raw[key]]
    match = []
    for yahoo_ind, yahoo_url in enumerate(yahoo_clean):
        for google_ind, google_url in enumerate(google_clean):
            if yahoo_url == google_url:
                match.append((google_ind, yahoo_ind))
    rho = calculate_rho(match)
    stats[key] = {"Overlap": len(match), "Percent": len(match) / 10, "Rho": rho}
calculate_avg_stats(stats)
write_result(stats)

# with open('queries-yahoo.txt') as f:
#     lines = [line.rstrip() for line in f]
  
# print(lines)