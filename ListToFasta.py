import urllib.request

def seq_getter(*accession_numbers, filename = "fasta_file.txt"):
    '''
    This function takes any number of UniProt accession numbers as strings, and creates a file with the sequences in fasta format.
    This function offers similar functionality to what is seen on the UniProt website, but this approach saves time.
    Rather than searching for each accession number in the UniProt website, they can be entered in a list, and the file will be generated in a few seconds.
    '''
    
    url_list = []
    fasta_seq_list = []
    
    url_beggining = "https://www.uniprot.org/uniprot/"
    url_end = ".fasta"

    for i in accession_numbers:
        full_url = url_beggining + str(i) + url_end
        url_list.append(full_url)

    if filename[-4:] != ".txt":
        filename += ".txt"

    try:
        for url in url_list:
            with urllib.request.urlopen(url) as uniprot_query:
                fasta_seq = uniprot_query.read()
                fasta_seq_list.append(fasta_seq)
        uniprot_query.close()

        with open(filename, "w") as fasta_file:
            for seq in fasta_seq_list:
                fasta_file.write(seq.decode())
        fasta_file.close()
    except urllib.error.HTTPError:
        print("HTTPError: Please make sure your accession numbers are valid.")

    return None
        
