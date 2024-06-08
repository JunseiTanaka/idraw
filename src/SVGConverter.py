import json
import svgwrite
from svgwrite import cm, mm   
import textwrap
import subprocess
import os


"""TODO: delete this comments
UI shows informations of
-json_file_name
-path_svg_file_path
-path_svg_file_name_rule
-font_size
-font_family
-text_anchor
-paper_size_mm(w,l)
"""

class JSON2SVG:
    def __init__(self, json_file_name='adjectives.json',
                 path_svg_file_path,
                 json_dir_path = '/home/jimay/idraw/src/json',
                 svg_dir_path = '/home/jimay/idraw/src/svg',
                 font_size = 11 * 1.3 * (374 / 297),
                 font_family = 'Academy Engraved LET',
                 text_anchor = 'middle',
                 paper_width_mm = 374,
                 paper_hight_mm = 525
                 ):
        
        self.json_file_name = json_file_name
        self.json_dir_path = json_dir_path
        self.svg_dir_path = svg_dir_path
        self.art_texts = None
        
        self.font_size = font_size# pt, increase font size by 1.3 times
        self.paper_height = paper_height # mm, updated paper height
        self.paper_width = paper_width  # mm, updated paper width
        self.mm_per_pt = 0.351  # mm/pt

        self.header_height = 30  # mm, adjust as needed
        self.margin = 30  # mm, adjust as needed
        self.line_height = 15 * 1.3  # mm (adjust as needed), increase line height by 1.3 times

        self._load_json()
        if self.json_file_name == "adjectives.json":
            self.art_texts = self._remove_duplicated_adjectives(self.art_texts)
            self.art_texts = self._add_adjectives(self.art_texts)
            
        self.characters_per_line = self._calc_characters_per_line()
        self.lines_per_page = self._calc_lines_per_page()
        self.lines = self._split_texts_for_paper_width()

        
    def _load_json(self):
        """
        The texts for art is from json file.
        """
        with open(f'{self.json_dir_path}/{self.json_file_name}', 'r') as f:
            self.art_texts = json.load(f)
            return self.art_texts
    
    def _calc_characters_per_line(self):        
        """
        Calculate the number of characters per line based on the width of A3 paper and the font size
        Assume that each character is 0.6 times the font size (this is a rough estimate and may not be accurate for all fonts)
        """
        self.characters_per_line = int(self.paper_width / (self.font_size * self.mm_per_pt * 0.6)) * 1.2  # Increase the threshold by 5%
        return self.characters_per_line 
        
    def _calc_lines_per_page(self):
        """Calculate the number of lines per page based on the height of A3 paper and the font size"""
        self.lines_per_page = int((self.paper_height - self.header_height - 2*self.margin) / self.line_height)
        return self.lines_per_page 

    def _remove_duplicated_adjectives(self, cont):
        """
        This is only for the example json data, "adjectives.json"
        so if your art texts are not this, you need to consider this method.
        """
        no_duplicated_cont = list(set(cont))
        return no_duplicated_cont
    
    def _add_adjectives(self, adjectives):
        """
        This is only for the example json data, "adjectives.json"
        so if your art texts are not this, you need to consider this method.
        """
        # Add adjectives
        adjectives_text = ', '.join(adjectives)

        return adjectives_text 

    def _split_texts_for_paper_width(self):
        wrapped_text = textwrap.fill(self.art_texts, width=self.characters_per_line)

        # Add each line of wrapped text as a separate SVG text element
        self.lines = wrapped_text.split('\n')

        return self.lines

    def create_svg(self):
        for i in range(0, len(self.lines), self.lines_per_page):
            # Create an SVG drawing
            dwg = svgwrite.Drawing(f'{self.svg_dir_path}/svg_{i//self.lines_per_page+1:02}.svg', profile='tiny', size=('374mm', '525mm'))  # updated paper size

            # Add header on the first page
            if i == 0:
                header = dwg.text('Self-confessed-critic', insert=(187*mm, 30*mm))  # center of updated paper size
                header['text-anchor'] = 'middle'
                header['font-size'] = '24pt'
                header['font-family'] = 'Academy Engraved LET'
                dwg.add(header)

            # Add lines
            for j, line in enumerate(self.lines[i:i+self.lines_per_page]):
                text_element = dwg.text(line, insert=(30*(374/297)*mm, (60 + j*self.line_height)*mm))  # adjust y position for each line
                text_element['font-size'] = f'{self.font_size}pt'
                text_element['font-family'] = 'Academy Engraved LET'
                dwg.add(text_element)

            # Save SVG
            dwg.save()

class SVG2PathSVG:
    def __init__(self):
        self.svg_dir_path = "/home/jimay/idraw/src/svg/"
        self.path_svg_dir_path = "/home/jimay/idraw/src/path_svg/"
        
        self.svg_files = self._get_svg_files()
        
    def _get_svg_files(self):
        svg_files = []
        # 指定されたディレクトリ内のファイルを取得
        for filename in os.listdir(self.svg_dir_path):
            # ファイルが.svg拡張子を持つか確認
            if filename.endswith(".svg"):
                # ファイルの絶対パスをリストに追加
                svg_files.append(os.path.join(filename))

            svg_files.sort()
                
        return svg_files
     

    def create_path_svg(self):
        for svg_file in self.svg_files:
            command = [
                'inkscape',
                self.svg_dir_path + svg_file,
                '--export-text-to-path',
                '--export-filename=' + self.path_svg_dir_path + str("path_") + svg_file
            ]
            print(self.path_svg_dir_path + str("path_") + svg_file)
            try:
                result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print("Command executed successfully")
                
            except subprocess.CalledProcessError as e:
                print("Error executing command")
                print("stdout:", e.stdout.decode())
                print("stderr:", e.stderr.decode())

if __name__ == "__main__":
    svg_converter = JSON2SVG("adjectives.json")
    svg_data = svg_converter.create_svg()
    
    path_svg_converter = SVG2PathSVG()
    path_svg_converter.create_path_svg()


