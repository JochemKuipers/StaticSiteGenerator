from textnode import TextNode, TextType
import re

def text_to_nodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
    # Split text into nodes based on markdown delimiters

    

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            text = node.text
            while delimiter in text:
                index = text.index(delimiter)
                before_text = text[:index]
                if before_text:  # Only add non-empty text before delimiter
                    new_nodes.append(TextNode(before_text, TextType.TEXT))

                # Special handling for image/link delimiters
                if delimiter.startswith('![') and delimiter.endswith('](') or delimiter.startswith('[') and delimiter.endswith(']('):
                    bracket_close = text.find(']', index)
                    paren_open = text.find('(', bracket_close)
                    paren_close = text.find(')', paren_open)
                    
                    if bracket_close == -1 or paren_open == -1 or paren_close == -1:
                        new_nodes.append(TextNode(text[index:], TextType.TEXT))
                        break
                    
                    url = text[paren_open + 1:paren_close]
                    if url:
                        new_nodes.append(TextNode(url, text_type))
                    text = text[paren_close + 1:]
                else:
                    text = text[index + len(delimiter):]
                    end_index = text.find(delimiter)
                    if end_index >= 0:
                        marked_text = text[:end_index]
                        if marked_text:  # Only add non-empty marked text
                            new_nodes.append(TextNode(marked_text, text_type))
                        text = text[end_index + len(delimiter):]
            if text:  # Only add remaining text if non-empty
                new_nodes.append(TextNode(text, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    # Extract text and URLs from image links using regex
    return re.findall(r'!\[(.*?)\]\((.*?)\)', text)

def extract_markdown_links(text):
    # Extract text and URLs from links using regex
    return re.findall(r'\[(.*?)\]\((.*?)\)', text)

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        curr_index = 0
        text = node.text
        links = extract_markdown_links(text)

        for link_text, url in links:
            # Find the full markdown link in the text
            full_link = f"[{link_text}]({url})"
            link_index = text.find(full_link, curr_index)
            
            # Add text before the link
            if link_index > curr_index:
                new_nodes.append(TextNode(text[curr_index:link_index], TextType.TEXT))
            
            # Add the link node
            new_nodes.append(TextNode(link_text, TextType.LINKS, url))
            
            curr_index = link_index + len(full_link)

        # Add remaining text after last link
        if curr_index < len(text):
            new_nodes.append(TextNode(text[curr_index:], TextType.TEXT))

    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        curr_index = 0
        text = node.text
        images = extract_markdown_images(text)

        for alt_text, url in images:
            # Find the full markdown image in the text
            full_image = f"![{alt_text}]({url})"
            image_index = text.find(full_image, curr_index)
            
            # Add text before the image
            if image_index > curr_index:
                new_nodes.append(TextNode(text[curr_index:image_index], TextType.TEXT))
            
            # Add the image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGES, url))
            
            curr_index = image_index + len(full_image)

        # Add remaining text after last image
        if curr_index < len(text):
            new_nodes.append(TextNode(text[curr_index:], TextType.TEXT))

    return new_nodes