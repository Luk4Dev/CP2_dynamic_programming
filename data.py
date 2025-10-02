# Autor: Diego
# data.py - Dados fictícios de estações e conexões

stations = {
    "Kings Cross": (51.5308, -0.1238),
    "Euston": (51.5281, -0.1337),
    "Russell Square": (51.5246, -0.1243),
    "Holborn": (51.5171, -0.1180),
    "Covent Garden": (51.5129, -0.1240),
    "Oxford Circus": (51.5154, -0.1419),
    "Piccadilly Circus": (51.5101, -0.1337),
    "Green Park": (51.5069, -0.1428),
    "Victoria": (51.4964, -0.1447)
}

edges = [
    ("Kings Cross", "Russell Square", "Piccadilly"),
    ("Russell Square", "Holborn", "Piccadilly"),
    ("Holborn", "Covent Garden", "Piccadilly"),
    ("Covent Garden", "Oxford Circus", "Piccadilly"),
    ("Oxford Circus", "Piccadilly Circus", "Bakerloo"),
    ("Piccadilly Circus", "Green Park", "Piccadilly"),
    ("Oxford Circus", "Green Park", "Victoria"),
    ("Green Park", "Victoria", "Victoria"),
    ("Kings Cross", "Euston", "Northern"),
    ("Euston", "Oxford Circus", "Central")
]
