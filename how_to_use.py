import fasta_parser

#let's say that you have a list of files in the format that you showed me earlier

#for example: dog.afa cat.afa potato.afa

#put them in a list

mylist = ["dog.afa","cat.afa","potato.afa"]

#then pass this to the parser

mydata = fasta_parser.fasta_parser(mylist)

#mydata will have the form of a dictionary of species,
#each species being a dictionary of proteins
#all data types are string
#below is an example of what mydata might look like

exampledata = {
            'dog': {'protein1': 'PROTEINDATAPROTEINDATAPROTEINDATAPROTEINDATA', 'mammal_protein': 'IMAMAMMALIMAMAMMALIMAMAMMALIMAMAMMAL'},
            'cat': {'protein1': 'PROTEINDATAPROTEINDATAPROTEINDATAPROTEINDATA', 'mammal_protein': 'IMAMAMMALIMAMAMMALIMAMAMMALIMAMAMMAL'},
            'potato': {'protein1': 'PROTEINDATAPROTEINDATAPROTEINDATAPROTEINDATA', 'mammal_protein': 'NUIFNIUQNFJENFQUIFNKFNWEKFNUIWENFUIU'}
            }
