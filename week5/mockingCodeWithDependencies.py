def getCommits(user, repo):
  getcommits_url = "https//api.github.com/repos" + user + "/" + repo + "/commits"

  resp = requests.get(getcommits_url) # requests.get() introduces external dependence; function want to mock
  repos_json = resp.text
  repos = json.loads(repos_json)
  result = []
  for item in repos:
    result.append(item['sha'])
  return result

# Unit Test without Mocking

def testGetNumberOfCommits(self):
  commits = getCommits(self.user, self.repo)  # Which makes testing In isolation difficult
  self.assertEqual(len(commits), 8)

@mock.patch('requests.get') # Use @Patch to mock requests.get(0 method)
  def testGetNumberOfCommits(self, mockedReq):  # this object will be called instead of requests.get()
    mockedReq.return_value = MockResponse('[{"sha": 1}, {"sha": 2}...{"sha":8}]') # return_value allows to "specify" behavior of mocked function; request.get will then always return this value. And it will NOT connect to any server
    commits = getCommits(self.user, self.repo)
    self.assertEqual(len(commits), 8)