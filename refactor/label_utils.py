import re


def clean_label(value):

    value = str(value).strip()

    value = re.sub(
        r'[^a-zA-Z0-9]',
        '_',
        value
    )

    if value[0].isdigit():
        value="_"+value

    return value


def generate_labels(
    property_name,
    value,
    pbn=False
):

    if value is None:
        return []

    value=str(value).strip()

    # tahun
    if property_name in ["birth", "death", "year"]:

        if pbn:
            return [f"year_{value}"]

        if property_name == "year":
            return [f"year_{value}"]

        if property_name == "birth":
            return [f"birth_{value}"]

        if property_name == "death":
            return [f"death_{value}"]


    # multiple value
    separators=[",",";"]

    values=[value]

    for sep in separators:

        if sep in value:

            values=[
                v.strip()
                for v in value.split(sep)
                if v.strip()
            ]

            break


    # kalau dipisah spasi khusus category
    if property_name=="category":

        values=value.split()


    return [
        clean_label(v)
        for v in values
    ]