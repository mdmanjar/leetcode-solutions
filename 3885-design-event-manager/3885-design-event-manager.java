
    class Node {
    int id;
    int priority;
    boolean active;

    Node(int id, int p) {
      this.id = id;
      this.priority = p;
      this.active = true;
    }
  }
  class EventManager {
    Queue<Node> pq;
    Map<Integer, Node> mp = new HashMap<>();

    public EventManager(int[][] events) {
      pq = new PriorityQueue<>((p, q) -> {
        if (p.priority != q.priority)
          return q.priority - p.priority;
        return p.id - q.id;
      });

      for (int[] x : events) {
        var node = new Node(x[0], x[1]);
        pq.offer(node);
        mp.put(x[0], node);
      }
    }

    public void updatePriority(int id, int p) {
      if (this.mp.containsKey(id)) {
        this.mp.get(id).active = false;
        var node = new Node(id, p);
        this.mp.put(id, node);
        this.pq.offer(node);
      }
    }

    public int pollHighest() {
      while (!this.pq.isEmpty() && !this.pq.peek().active)
        this.pq.poll();
      if (this.pq.isEmpty())
        return -1;
      return this.pq.poll().id;
    }
  }