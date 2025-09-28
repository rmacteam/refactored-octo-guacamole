import json
import uuid

class Field:
    def __init__(self, name, field_type, required=False, options=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.type = field_type
        self.required = required
        self.options = options or []

class Form:
    def __init__(self, title):
        self.id = str(uuid.uuid4())
        self.title = title
        self.fields = []

    def add_field(self, field):
        self.fields.append(field)

    def remove_field(self, field_id):
        self.fields = [f for f in self.fields if f.id != field_id]

    def render(self):
        print(f"Form: {self.title}")
        for idx, f in enumerate(self.fields):
            if f.type == "text":
                print(f"{idx+1}. {f.name} [Text]{' (Required)' if f.required else ''}")
            elif f.type == "select":
                print(f"{idx+1}. {f.name} [Select]: {', '.join(f.options)}{' (Required)' if f.required else ''}")
            elif f.type == "checkbox":
                print(f"{idx+1}. {f.name} [Checkbox]{' (Required)' if f.required else ''}")

    def export_json(self):
        return json.dumps({
            "id": self.id,
            "title": self.title,
            "fields": [
                {
                    "id": f.id,
                    "name": f.name,
                    "type": f.type,
                    "required": f.required,
                    "options": f.options
                }
                for f in self.fields
            ]
        }, indent=2)

# Demo
if __name__ == "__main__":
    builder = Form("Registration")
    builder.add_field(Field("Name", "text", True))
    builder.add_field(Field("Email", "text", True))
    builder.add_field(Field("Country", "select", False, ["Indonesia", "Singapore", "Malaysia"]))
    builder.add_field(Field("Subscribe", "checkbox", False))
    builder.render()
    print("\nExported JSON:")
    print(builder.export_json())