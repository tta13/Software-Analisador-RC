import glob, os
import run

def get_files_by_extension(ext: str) -> list[str]:
    result = []
    for file in glob.glob(f'*.{ext}'):
        result.append(file)
    return result

def main():
    script_directory = os.getcwd()
    data_dir = os.path.join(script_directory, 'data')
    if(os.getcwd() != data_dir):
        os.chdir(data_dir)
    rcg_files = get_files_by_extension('rcg')
    rcl_files = get_files_by_extension('rcl')

    for rcg, rcl in zip(rcg_files, rcl_files):
        print(f'Running analysis: {rcg}, {rcl}...')
        run.run_analysis(os.path.join(data_dir, rcg), os.path.join(data_dir, rcl), os.path.join(data_dir, rcg.split('.')[0] + '.log.json'))
        print('Done!')
    print('Finished.')


if __name__ == '__main__':
    main()
