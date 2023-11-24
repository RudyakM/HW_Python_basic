from module import ParserWordPress

point = ParserWordPress()
r = point.requester()

if __name__ == '__main__':
    if r.status_code == 200:
        sections = point.get_all_data(r=r)
        point.get_info(sections=sections)
