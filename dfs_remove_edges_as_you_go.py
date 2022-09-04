class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        graph = defaultdict(list)
        num_tickets = len(tickets)
        ticket_dict = dict()
        for index, ticket in enumerate(tickets):
            src, dst = ticket
            graph[src].append((dst, index))  # store ticket number as well
            ticket_dict[index] = ticket

        # sort lexicographically TODO check syntax
        for key in graph.keys():
            graph[key].sort(key=lambda x: x[0], reverse=True)

        def dfs(start):
            ls = [(start, [])]  # store current node and tickets used so far in order
            while len(ls) > 0:
                cur, used_tickets = ls.pop()

                if len(used_tickets) == num_tickets:
                    return used_tickets  # we found one order, return this

                for neighbor, ticket_number in graph[cur]:
                    if ticket_number not in used_tickets:
                        new = used_tickets.copy()
                        new.append(ticket_number)
                        ls.append((neighbor, new))
            # given question, code should never reach here
            return []  # no such path found

        tickets = dfs("JFK")
        stops = ["JFK"]
        print(tickets)
        print(ticket_dict)
        for i in tickets:
            src, dst = ticket_dict[i]
            stops.append(dst)

        return stops