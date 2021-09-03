# Functions used in the DataGen Application
# This is a modified file to use in formbot application

import random
import csv


#  Process first names -- names then frequencies
def process_first_names(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        list_name = list(reader)
        gender_name = [row[0] for row in list_name]
        del gender_name[0]
    return gender_name


# Frequencies
def process_names_frequencies(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        list_name = list(reader)
        gender_frequency = [row[2] for row in list_name]
        del gender_frequency[0]
        gender_frequency = [int(i) for i in gender_frequency]
    return gender_frequency


# Process surnames
def process_surnames(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        surnamelist = list(reader)
        del surnamelist[0]
        surnames = [row[0].title() for row in surnamelist]
    return surnames


# Process surname cumulative Frequencies
def surname_cum_freq(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        surnamelist = list(reader)
        del surnamelist[0]
        surname_cum_freq1 = [float(row[4]) for row in surnamelist]
    return surname_cum_freq1


# New functions for `formbot` project


def random_name():
    #  Generate Customer List
    f_names = process_first_names('resources/first_names_f.csv')
    f_freq = process_names_frequencies('resources/first_names_f.csv')
    m_names = process_first_names('resources/first_names_m.csv')
    m_freq = process_names_frequencies('resources/first_names_m.csv')
    surnames = process_surnames('resources/Names_2010Census.csv')
    #surname_cum_freq = surname_cum_freq('resources/Names_2010Census.csv')
    # surname_cum_freq.pop()

    # Determine proportion of f/m
    size_f = 1000
    size_m = 1000

    # Choose first names
    first_names = []
    m_first_name = random.choices(m_names, weights=m_freq, k=size_m)
    f_first_name = random.choices(f_names, weights=f_freq, k=size_f)
    for name in m_first_name:
        first_names.append(name)
    for name in f_first_name:
        first_names.append(name)

    # Choose surnames
    surnames = random.choices(surnames, k=(size_f + size_m))

    # Choose addresses
    with open('resources/fake_addresses_3.csv') as f:
        reader = csv.reader(f)
        addresses = list(reader)
    del addresses[0]

    sample_addresses = random_index((size_f + size_m), addresses)
    street_address = [row[0] for row in sample_addresses]
    city = [row[1] for row in sample_addresses]
    state = [row[2] for row in sample_addresses]
    zipcode = [row[3] for row in sample_addresses]


    # Build master customer list
    customer_list = list(
        zip(first_names, surnames, street_address, city, state, zipcode))

    return customer_list

relations = ["sister",
             "brother",
             "cousin",
             "step-father",
             "step-mother",
             "hairdresser",
             "gun-salesman",
             "gunsmith",
             "truck fixer",
             "neice",
             "nephew",
             "granny",
             "government informant",
             "representative",
             "defensive back",
             "wife",
             "husband",
             "ex-wife",
             "ex-husband",
             "pappy",
             "mammy",
             "district manager",
             "kissin' cousin if you know what I mean",
             "drug dealer",
             "business partner",
             "financial planner",
             "friend the assistant manager at Arby's on 4th street",
             "member of congress",
             "gardner",
             "florist",
             "boss",
             "employer",
             "employee",
             "drummer",
             "hornswaggler",
             "pimp",
             "repubplican school board member",
             "idiot cousin",
             "veterinarian",
             "personal shopper",
             "minister",
             "yoga teacher,"
             "martial arts instructor",
             "sensei",
             "preacher",
             "Sunday School teacher"
           ]

interjections = ["you know the one",
                 "if you know what i mean",
                 "or something like that",
                 "anyway that's what they said",
                 "or so I'm told",
                 ]

told_me = [ "said",
            "told me",
            "though i needed to know",
            "wanted me to tell you",
            "and well damn if I didn't see it with my own eyes",
]

how_long = ["maybe a month",
            "last year",
            "gotta be what 3 months now",
            "like a month maybe",
            "7 weeks, two days",
            "don't know but baby done gonna come by christmas",
            "4 years",
            "only brrn two weeks but yuou gotta watch him",
            "long time now",
            "i dunno"]

business = ["Cracker Barrell",
            "7-11",
            "Papa John's",
            "gun factory",
            "Southwest Airlines headquarters",
            "McDonalds",
            "Pizza Hut",
            "Mobil station",
            "Chevron",
            "Ford dealership",
            "ammo store",
            "feed shop",
            "tractor supply",
            "chewing tobacco store",
            "taxedermist",
            "church",
            "holler",
            "gulch"]