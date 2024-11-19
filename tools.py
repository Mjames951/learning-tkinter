def check_options(widget):
    options = widget.configure()
    print("options for this widget: ")
    for option in options:
        print(f"\t{option}: \t{options[option]}")