class Logger {
  logs: { [key: string]: number };

  constructor() {
    this.logs = {};
  }

  shouldPrintMessage(timestamp: number, message: string): boolean {
    if (!(message in this.logs) || this.logs[message] <= timestamp) {
      this.logs[message] = timestamp + 10;
      return true;
    }

    return false;
  }
}
