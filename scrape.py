import requests

headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-GB,en;q=0.9",
    # 'Accept-Encoding': 'gzip, deflate, br',
    "Host": "wabi-europe-north-b-api.analysis.windows.net",
    "Origin": "https://app.powerbi.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15",
    "Referer": "https://app.powerbi.com/",
    # 'Content-Length': '2730',
    "Connection": "keep-alive",
    "X-PowerBI-ResourceKey": "1c68f5e9-d9ad-456c-9a11-85cf025279a1",
    "RequestId": "1d02f746-7d07-ea84-4e43-bf3f1df4cc6e",
    "ActivityId": "5e0afc21-0472-5cee-cf4f-e39c3de1c76e",
}

params = {
    "synchronous": "true",
}

json_data = {
    "version": "1.0.0",
    "queries": [
        {
            "Query": {
                "Commands": [
                    {
                        "SemanticQueryDataShapeCommand": {
                            "Query": {
                                "Version": 2,
                                "From": [
                                    {
                                        "Name": "f",
                                        "Entity": "Fyrir vef",
                                        "Type": 0,
                                    },
                                ],
                                "Select": [
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "f",
                                                },
                                            },
                                            "Property": "Kennitala",
                                        },
                                        "Name": "Fyrir vef.Kennitala",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "f",
                                                },
                                            },
                                            "Property": "Námsbraut",
                                        },
                                        "Name": "Fyrir vef.Námsbraut",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "f",
                                                },
                                            },
                                            "Property": "Námsleið",
                                        },
                                        "Name": "Fyrir vef.Námsleið",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "f",
                                                },
                                            },
                                            "Property": "Útgáfuár",
                                        },
                                        "Name": "Fyrir vef.Útgáfuár",
                                    },
                                    {
                                        "Aggregation": {
                                            "Expression": {
                                                "Column": {
                                                    "Expression": {
                                                        "SourceRef": {
                                                            "Source": "f",
                                                        },
                                                    },
                                                    "Property": "Hæfniþrep",
                                                },
                                            },
                                            "Function": 0,
                                        },
                                        "Name": "Sum(Fyrir vef.Hæfniþrep)",
                                    },
                                    {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Source": "f",
                                                },
                                            },
                                            "Property": "Námslýsing",
                                        },
                                        "Name": "Fyrir vef.Námslýsing",
                                    },
                                ],
                                "OrderBy": [
                                    {
                                        "Direction": 1,
                                        "Expression": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Source": "f",
                                                    },
                                                },
                                                "Property": "Námsbraut",
                                            },
                                        },
                                    },
                                ],
                            },
                            "Binding": {
                                "Primary": {
                                    "Groupings": [
                                        {
                                            "Projections": [
                                                0,
                                                1,
                                                2,
                                                3,
                                                4,
                                                5,
                                            ],
                                        },
                                    ],
                                },
                                "DataReduction": {
                                    "DataVolume": 3,
                                    "Primary": {
                                        "Window": {
                                            "Count": 500,
                                        },
                                    },
                                },
                                "Version": 1,
                            },
                            "ExecutionMetricsKind": 1,
                        },
                    },
                ],
            },
            "CacheKey": '{"Commands":[{"SemanticQueryDataShapeCommand":{"Query":{"Version":2,"From":[{"Name":"f","Entity":"Fyrir vef","Type":0}],"Select":[{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"Kennitala"},"Name":"Fyrir vef.Kennitala"},{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"Námsbraut"},"Name":"Fyrir vef.Námsbraut"},{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"Námsleið"},"Name":"Fyrir vef.Námsleið"},{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"Útgáfuár"},"Name":"Fyrir vef.Útgáfuár"},{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"Hæfniþrep"}},"Function":0},"Name":"Sum(Fyrir vef.Hæfniþrep)"},{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"Námslýsing"},"Name":"Fyrir vef.Námslýsing"}],"OrderBy":[{"Direction":1,"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"Námsbraut"}}}]},"Binding":{"Primary":{"Groupings":[{"Projections":[0,1,2,3,4,5]}]},"DataReduction":{"DataVolume":3,"Primary":{"Window":{"Count":500}}},"Version":1},"ExecutionMetricsKind":1}}]}',
            "QueryId": "",
            "ApplicationContext": {
                "DatasetId": "b84e06f3-7624-4b3f-aae5-839815202a3b",
                "Sources": [
                    {
                        "ReportId": "48ca4581-fee1-4219-bbc5-17f8024ae474",
                        "VisualId": "83693454521ac6b1edbd",
                    },
                ],
            },
        },
    ],
    "cancelQueries": [],
    "modelId": 5778628,
}

response = requests.post(
    "https://wabi-europe-north-b-api.analysis.windows.net/public/reports/querydata",
    params=params,
    headers=headers,
    json=json_data,
)

import re

links = re.findall(
    r"https:\/\/namskra\.is\/programmes\/[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}",
    response.text,
)

for link in set(links):
    response = requests.get(link + "/json")
    print(link)
    data = response.json()
    if data.get("_id"):
        with open(f'.dumps/{data["_id"]}.json', "w") as fp:
            fp.write(response.text)
