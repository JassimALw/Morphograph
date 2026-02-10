import graph_and_vertex as gv
import data as d

g = gv.Graph()

for item in d.test_data:
    v = gv.Vertex(
        item["word"],
        item["definition"],
        item["type2"],
        item["kind"],
        item.get("prefix", "No prefix"),
        item.get("root", "No root"),
        item.get("suffix", "No suffix")
    )
    g.add_vertex(v)

for name, v in g.vertices.items():
    print(name, "->", v.kind)
