import warnings
warnings.filterwarnings("ignore")
from parrot import Parrot
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")
phrases = ["Can you recommed some upscale restaurants in Rome?"]
for phrase in phrases:
  print("-"*100)
  print(phrase)
  print("-"*100)
  para_phrases = parrot.augment(input_phrase=phrase,
                                use_gpu=False,
                                diversity_ranker="levenshtein",
                                do_diverse=False, 
                                max_return_phrases = 10, 
                                max_length=32, 
                                adequacy_threshold = 0.99, 
                                fluency_threshold = 0.90)
  for paraphrase in para_phrases:                                  
      print(paraphrase)                               

 
  
