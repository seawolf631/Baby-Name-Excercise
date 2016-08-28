
import sys
import re

"""Baby Names exercise"""

def extract_year(filename):
  for x in range(len(filename)):
    file = open(filename, 'r')
    content = file.read()
    year = re.findall('Popularity in (\d\d\d\d)', content)
    return year[0]
def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  file = open(filename, 'r')
  content = file.read()
  year = extract_year(filename)
  boys = re.findall('<td>(\d+)</td><td>(\w+)</td>', content)
  girls = re.findall('<td>(\d+)</td><td>\w+</td><td>(\w+)</td>', content)
  finalList = [year]
  for x in range(0,len(boys)):
    finalList.append(boys[x][1] +" "+ str(x+1))
    finalList.append(girls[x][1] +" "+ str(x+1))
  return sorted(finalList)


def main():
  
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  
  # For each filename, get the names, then either print the text output
  
  for x in range(0,len(args)):
    myList = extract_names(args[x])
    text = '\n'.join(myList) + '\n'
    f = open(args[x] + ".summary", 'w')
    f.write(text)
    f.close

if __name__ == '__main__':
  main()
