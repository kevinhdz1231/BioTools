import urllib.request

def seq_getter(accession_number, filename):
    '''
    This function takes a UniProt accession number and returns the sequencein a fasta file.
    It takes two string arguments.
    One is the UniProt accession number, and the other is the name of the txt file that will be generated.
    '''
    
    url_beggining = "https://www.uniprot.org/uniprot/"
    url_end = ".fasta"
    full_url = url_beggining + str(accession_number) + url_end

    try:
        with urllib.request.urlopen(full_url) as uniprot_query:
            fasta_seq = uniprot_query.read()
            uniprot_query.close()

        if filename[-4:] != ".txt":
            filename += ".txt"

        with open(filename, "w") as fasta_file:
            fasta_file.write(fasta_seq.decode())
    except urllib.error.HTTPError as err:
            print("HTTPError: Please make sure your UniProt accession number is valid.")

    return None









