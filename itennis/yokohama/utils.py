
def get_button_id_from_court_name(name):
    pair = {"ushioda": "fbox_110",
            "irifune": "fbox_120",
            "mitsuzawa": "fbox_150",
            "shimizu": "fbox_310",
            "shinyoko": "fbox_570"}
    return pair[name]
