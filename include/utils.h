#include <functional>
#include <string>
#include <vector>

namespace utils {
std::vector<std::string> split(const std::string& string, char character);

template <typename K, typename V>
std::vector<V> map(std::vector<K> original, std::function<V(K)> fn) {
  std::vector<V> output;

  for (K val : original) {
    output.push_back(fn(val));
  }

  return output;
};
}  // namespace utils