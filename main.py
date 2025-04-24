from tools.parser import get_google_sheet_data, save_data_to_file 
from tools.visualizer import Visualizer


def main():
    spreadsheet_id = '1RfAnpdQZ8ow1Cb4B8WjJbNO79QX0Ii0OkuG7XFJMh3Y'
    sheet_id = '69322794'

    data = get_google_sheet_data(spreadsheet_id, sheet_id)
    save_data_to_file(data)

    visualizer = Visualizer(data)
    visualizer.plot_all()


if __name__ == '__main__':
    main()

