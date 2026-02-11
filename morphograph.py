class Vertex:   
    #create vertex word: the word itself, difinition: common do I need to clarify what it is!, type2: noun, verb, adjective or an adverb, kind in case it's a stand alone word, prefix, suffix
    def __init__(self, word:str, definition:str ,type2:str, kind:str,
         prefix:str = "No prefix", root:str = "No root", suffix:str = "No suffix"): #No vertex-level relation  (those belong to edges)
        self.word = word
        self.definition = definition
        self.type2 = type2 # noun/ verb whatever!
        self.kind = kind # word, affixes or a root :D
        self.prefix = prefix
        self.root = root
        self.suffix = suffix
        self.adjacent = {
            "has_prefix" : [],
            "has_root" : [],
            "has_suffix":[]
        } # family: {relation: [objects]}

    # Private Helper method DO NOT CALL use useless method instead
    def _adjoin(self,vertex, has_prefix:bool = False , has_root:bool = False, has_suffix:bool = False):
        if has_prefix:
            self.adjacent["has_prefix"].append(vertex)
        if has_root:
            self.adjacent["has_root"].append(vertex)
        if has_suffix:
            self.adjacent["has_suffix"].append(vertex)

    
class Graph:
    # Stores all vertices by name.
    def __init__(self):
        self.vertices = {} # {name: Vertex}
        #hmmmmmmmm
        self.prefix_reverse ={}
        self.root_reverse = {}
        self.suffix_reverse={}
    

    #Private method
    def _reverse_look_up(self, relation:str, key_word:str, word_vertex):
        if relation == "root":
            self.root_reverse.setdefault(key_word, []).append(word_vertex)
        if relation == "prefix":
            self.prefix_reverse.setdefault(key_word, []).append(word_vertex)
        if relation == "suffix":
            self.suffix_reverse.setdefault(key_word, []).append(word_vertex)
    
     
    # Private method: to ensure value inserted is an object of Vertex; returns object of vertex
    def _ensure_vertex(self, value):
        if not isinstance(value, (Vertex, str)):
            raise TypeError("This method only handles Vertex Objects and STR")
        #Case 1: already a Vertex
        if isinstance(value, Vertex):
             if value.word not in self.vertices:
                self.vertices[value.word] = value
             return value
        #Case 2: not a vertex
        if value in self.vertices:
            return self.vertices[value]
        # Case 3: creates a new Vertex
        v = Vertex(word = value,
                   definition = "No definition",
                   type2 = "affix",
                   kind = "affix") 
        self.vertices[value] = v
        return v
        
    #Private method
    def _link(self, word_vertex, relation: str, affix_name: str):
        if affix_name in (None, "No prefix", "No root", "No suffix"):
            return None
        affix_vertex = self._ensure_vertex(affix_name)
        
        #Case 1: PREFIX, I hope it doesn't malfunction again!
        if relation == "prefix":
            word_vertex._adjoin(affix_vertex, has_prefix = True)
            self.prefix_reverse.setdefault(affix_name, []).append(word_vertex)
        
        #Case 2: ROOT.
        elif relation == "root":
            word_vertex._adjoin(affix_vertex, has_root = True)
            self.root_reverse.setdefault(affix_name, []).append(word_vertex)
            
        #Case 3: SUFFIX
        elif relation == "suffix":
            word_vertex._adjoin(affix_vertex, has_suffix = True)
            self.suffix_reverse.setdefault(affix_name, []).append(word_vertex)
          
    #Public method: normalizes input and adds a vertex using ensure_vertex()
    def add_vertex(self, vertex:Vertex):
        word = self._ensure_vertex(vertex)
        self._link(word, "prefix", word.prefix)
        self._link(word, "root", word.root)
        self._link(word, "suffix", word.suffix)
        return word
