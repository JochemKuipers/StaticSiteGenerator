class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props if props else {}
        
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, value:str, tag:str=None, props:dict=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value")
        if not self.tag:
            return self.value
        props_string = self.props_to_html()
        props_html = f" {props_string}" if props_string else ""
        if self.tag == "img":
            return f"<{self.tag}{props_html}>"
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        return f"<{self.tag} {self.props_to_html()}>{''.join(
            [
                child.to_html() if isinstance(child, HTMLNode) else child for child in self.children
            ])}</{self.tag}>"