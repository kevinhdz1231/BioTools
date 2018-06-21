class Seq:

    DNA_bases = ['A','T','G','C']
    RNA_bases = ['A','U','G','C']
    amino_acids = ['A','R','N','D','B','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']
    
    def __init__(self, sequence, seq_type):

        if seq_type.upper() == "DNA":
            for base in sequence:
                if base not in DNA_bases:
                    print("Error: please make sure that your DNA sequence contains only A,T,C, and G.")
                    return
            self.sequence = sequence.upper()
            self.seq_type = seq_type
            return

        elif seq_type == "RNA":
            for base in sequence:
                if base not in RNA_bases:
                    print("Error: please make sure that your RNA sequence contains only A,U,C, and G.")
                    return
            self.sequence = sequence.upper()
            self.seq_type = seq_type

        elif seq_type == "Prot":
            for base in sequence:
                if base not in amino_acids:
                    print("Make sure that your protein sequence has proper amino acid abbreviations in it.")
                    return
            self.sequence = sequence.upper()
            self.seq_type = seq_type



    def __repr__(self):

        return self.sequence



    def __str__(self): # redundant

        return self.sequence


    def transcribe(self):
        """" This function transcribes a DNA string into an RNA string """

        if self.seq_type == "DNA":
            return self.sequence.replace('T','U')

        else:
            print("You can only transcribe a DNA object.")


    def translate(self):
        """ This function translates a RNA sequence into a protein sequence """
        













